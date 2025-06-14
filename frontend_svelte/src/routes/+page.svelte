<script lang="ts">
    import { onMount } from 'svelte';

    let rhymeGroups: any[] = [];

    onMount(async () => {
        const res = await fetch('/api/rhyme-groups');
        if (res.ok) {
            rhymeGroups = await res.json();
        } else {
            console.error('Failed to fetch rhyme groups');
        }
    });
</script>

<h1>RapTrainer</h1>

{#if rhymeGroups.length > 0}
    <ul>
        {#each rhymeGroups as group}
            <li>{group.name} ({group.word_count} words)</li>
        {/each}
    </ul>
{:else}
    <p>Loading rhyme groups...</p>
{/if} 