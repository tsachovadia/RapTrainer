import json
from rich.console import Console
from rich.prompt import Prompt
from phonikud import predict
import hebrew_tokenizer as ht
import random

console = Console()

def load_words():
    """Loads the word list from the CSV file."""
    console.log("Loading word list...")
    words = []
    with open("rhyme_trainer/word_list.csv", "r", encoding="utf-8") as f:
        # Skip header
        next(f)
        for line in f:
            try:
                # The word is the first value in the comma-separated line
                word = line.strip().split(",")[0]
                # We only want words with 2 or more characters
                if len(word) > 1:
                    words.append(word)
            except IndexError:
                # Skip empty or malformed lines
                continue
    console.log(f"Loaded {len(words)} words.")
    return words

def get_phonetic_info(word):
    """Gets phonetic info for a word using phonikud."""
    # Phonikud expects a tokenized input
    tokens = ht.tokenize(word)
    # We are interested in the first token (the word itself)
    word_tokens = [t[1] for t in tokens if t[0] == 'HEBREW']

    if not word_tokens:
        return {
            "nikud": word,
            "phonetics": "",
            "syllables": 0,
            "commonness": "Unknown"
        }

    # Predict the nikud and phonemes
    nikud, phonemes, _ = predict(word_tokens)
    
    # Estimate syllable count by counting vowels in phonemes
    syllables = sum(1 for char in phonemes if char in "aeiou")

    return {
        "nikud": nikud,
        "phonetics": phonemes,
        "syllables": syllables,
        "commonness": "Unknown" # We will implement this later
    }

def display_analysis(seed_word, seed_info, candidate_word, candidate_info):
    """Displays the analysis of the word pair using rich Table."""
    from rich.table import Table

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Property", style="dim")
    table.add_column(seed_word, style="bold green")
    table.add_column(candidate_word, style="bold yellow")

    table.add_row("Nikud", seed_info['nikud'], candidate_info['nikud'])
    table.add_row("Phonetics (IPA)", seed_info['phonetics'], candidate_info['phonetics'])
    table.add_row("Syllables", str(seed_info['syllables']), str(candidate_info['syllables']))
    
    console.print(table)

def rate_rhyme():
    """Prompts the user to rate the rhyme."""
    return Prompt.ask(
        "How good is this rhyme? (1-5)",
        choices=["1", "2", "3", "4", "5"],
        show_choices=True,
        default="3"
    )

def rate_register():
    """Prompts the user to rate the word register."""
    return Prompt.ask(
        "How would you classify the word register? (1-4)",
        choices=["1", "2", "3", "4"],
        show_choices=True,
        default="1"
    )

def save_data(data, seed_word_info, candidate_word_info, rhyme_rating, register_rating):
    """Saves the collected data to a JSON file."""
    record = {
        "seed_word": seed_word_info,
        "candidate_word": candidate_word_info,
        "ratings": {
            "rhyme_quality": rhyme_rating,
            "register": register_rating
        }
    }
    data.append(record)
    with open("rhyme_trainer/rhyme_training_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    console.log(f"[bold green]Saved rating for {seed_word_info['nikud']} vs {candidate_word_info['nikud']}[/bold green]")

def main():
    """Main function for the Rhyme Trainer CLI."""
    console.print("[bold cyan]Welcome to the RapTrainer Rhyme Engine Trainer![/bold cyan]")
    
    try:
        with open("rhyme_trainer/rhyme_training_data.json", "r", encoding="utf-8") as f:
            training_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        training_data = []
    
    # 1. Load our dictionary
    word_list = load_words()
    # Let's shuffle the list to get different words each time
    random.shuffle(word_list)
    
    # 2. Get a seed word from the user
    seed_word = Prompt.ask("Enter a word to find rhymes for")
    
    # 3. Get phonetic info for the seed word
    seed_word_info = get_phonetic_info(seed_word)
    
    console.print(f"\nFinding rhymes for [bold green]{seed_word}[/bold green]...")

    # Main training loop
    for candidate_word in word_list:
        if candidate_word == seed_word:
            continue

        console.rule(f"Candidate: [bold yellow]{candidate_word}[/bold yellow]")
        
        # Get phonetic info for the candidate
        candidate_word_info = get_phonetic_info(candidate_word)
        
        # Display the analysis (to be implemented)
        display_analysis(seed_word, seed_word_info, candidate_word, candidate_word_info)
        
        # Get user ratings
        rhyme_rating = int(rate_rhyme())
        register_rating = int(rate_register())
        
        # Save the data to a JSON file
        save_data(training_data, seed_word_info, candidate_word_info, rhyme_rating, register_rating)

        # Ask to continue
        if not Prompt.ask("\nContinue with next word?", default="y").lower().startswith("y"):
            break
            
    console.print("\n[bold magenta]Training session complete. Thank you![/bold magenta]")


if __name__ == "__main__":
    main()
