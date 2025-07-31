<script setup>
import { Toast } from 'primevue';
import { onMounted } from 'vue'
import { initFlowbite } from 'flowbite'

// initialize components based on data attribute selectors
onMounted(() => {
    initFlowbite();
})

</script>
<template>
  <Toast />
  <router-view></router-view>
</template>