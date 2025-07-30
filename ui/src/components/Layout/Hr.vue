<template>
    <nav>
        <router-link :to="{name: 'hr-dashboard'}" class="text-blue-500 underline">HR Dashboard</router-link>
    </nav>
    <div class="container mx-auto">
        <router-view></router-view>
    </div>
</template>