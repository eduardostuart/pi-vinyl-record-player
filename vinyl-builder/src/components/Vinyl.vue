<script lang="ts" setup>
import RecordGroove from "./RecordGroove.vue";
defineProps<{
  src?: string;
}>();
</script>
<template>
  <div
    class="w-full h-full bg-zinc-100 mx-auto border border-black rounded-full relative overflow-hidden"
  >
    <div
      class="w-[1cm] h-[1cm] absolute mx-auto my-auto z-20 inset-0 bg-white rounded-full border-2 border-black/80"
    ></div>
    <RecordGroove
      class="absolute z-10 opacity-40 left-0 top-0 right-0 bottom-0 w-full h-full rounded-full"
    />
    <img v-show="src" class="w-full h-full" :src="src" />
  </div>
</template>
