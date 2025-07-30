<script setup>
import InputText from '@/volt/InputText.vue';
</script>
<template>
    <div class="w-screen h-screen flex flex-col justify-center items-center">
        <h1 class="mx-auto">Login Page</h1>
        <form class="max-w-md min-w-md" >
            <div class="relative w-full">
                <i class="pi pi-search absolute top-1/2 -mt-2 text-surface-400 leading-none start-3 z-1" />
                <InputText placeholder="Search" pt:root="ps-10" />
            </div>
        </form>
    </div>
</template>