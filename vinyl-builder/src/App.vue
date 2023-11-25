<script setup lang="ts">
import { VinylBuilder } from "@/components";
</script>
<template>
  <div>
    <div
      class="w-[21.0cm] h-[29.7cm] p-10 overflow-hidden shadow px-4 bg-zinc-50"
    >
      <VinylBuilder v-for="idx in 3" class="mb-4 mx-auto" :key="idx" />
    </div>
  </div>
</template>
