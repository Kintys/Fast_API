<script setup>
import AppNavbar from "@/components/layout/AppNavbar.vue";
</script>

<template>
  <div class="min-h-screen bg-slate-50">
    <AppNavbar />
    <main class="py-8">
      <RouterView />
    </main>
  </div>
</template>
