<script setup>
import { RouterLink } from "vue-router";
import AppContainer from "@/components/layout/AppContainer.vue";
</script>

<template>
  <AppContainer>
    <section class="py-12 text-center sm:py-16">
      <h1 class="text-3xl font-semibold tracking-tight text-slate-900 sm:text-4xl">
        Booking System
      </h1>
      <p class="mx-auto mt-3 max-w-xl text-base text-slate-600">
        Find and book a room for your next meeting or event.
      </p>
      <RouterLink
        to="/rooms"
        class="mt-8 inline-flex rounded-md bg-slate-900 px-5 py-2.5 text-sm font-medium text-white transition hover:bg-slate-800"
      >
        Browse rooms
      </RouterLink>
    </section>
  </AppContainer>
</template>
