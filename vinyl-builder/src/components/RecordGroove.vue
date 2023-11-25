<script lang="ts" setup>
// A component that generates a SVG similar to a record's groove.
import { computed } from "vue";

const lines = computed(() => {
  const lines = [];
  for (let i = 0; i < 210; i++) {
    if (i % 10 === 0) {
      lines.push(i);
    }
  }
  return lines;
});
</script>
<template>
  <svg
    width="400px"
    height="400px"
    viewBox="0 0 400 400"
    xmlns="http://www.w3.org/2000/svg"
  >
    <g transform="translate(200,200)">
      <circle
        v-for="i in lines"
        :key="i"
        cx="0"
        cy="0"
        :r="i"
        stroke="black"
        stroke-width="1"
        fill="none"
      />
    </g>
  </svg>
</template>
