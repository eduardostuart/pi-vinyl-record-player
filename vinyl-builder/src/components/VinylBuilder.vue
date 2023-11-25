<script setup lang="ts">
import Vinyl from "./Vinyl.vue";
import { ref } from "vue";

const images = ref<{
  front?: string;
  back?: string;
}>({});

function preview(e: Event, side: "front" | "back") {
  const reader = new FileReader();
  reader.addEventListener(
    "load",
    () => {
      const img = reader.result!.toString();
      images.value[side] = img;
      if (side === "front" && !images.value.back) {
        images.value.back = img;
      }
    },
    false
  );
  const target = e.target as HTMLInputElement;
  if (target?.files?.length) {
    const file = target.files[0];
    if (file) {
      reader.readAsDataURL(file);
    }
  }
}
</script>
<template>
  <div class="w-full">
    <div class="flex flex-row justify-center gap-4">
      <label class="text-center block w-[8cm] h-[8cm]">
        <input type="file" class="hidden" @change="preview($event, 'front')" />
        <Vinyl :src="images.front" />
      </label>
      <label class="text-center block w-[8cm] h-[8cm]">
        <input type="file" class="hidden" @change="preview($event, 'back')" />
        <Vinyl :src="images.back" />
      </label>
    </div>
  </div>
</template>
