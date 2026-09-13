<script setup>
import { RouterLink } from "vue-router";

// TODO: show user name and Logout after authentication
// TODO: show Admin links for admin role
</script>

<template>
  <header class="border-b border-slate-200 bg-white">
    <div
      class="mx-auto flex max-w-7xl items-center justify-between px-4 py-4 sm:px-6 lg:px-8"
    >
      <RouterLink
        to="/"
        class="text-lg font-semibold tracking-tight text-slate-900"
      >
        Booking System
      </RouterLink>

      <nav class="flex items-center gap-6 text-sm font-medium">
        <RouterLink
          to="/rooms"
          class="text-slate-600 transition hover:text-slate-900"
          active-class="text-slate-900"
        >
          Rooms
        </RouterLink>
        <RouterLink
          to="/rooms/new"
          class="text-slate-600 transition hover:text-slate-900"
          active-class="text-slate-900"
        >
          Add room
        </RouterLink>
        <RouterLink
          to="/my-bookings"
          class="text-slate-600 transition hover:text-slate-900"
          active-class="text-slate-900"
        >
          My Bookings
        </RouterLink>
        <RouterLink
          to="/login"
          class="text-slate-600 transition hover:text-slate-900"
          active-class="text-slate-900"
        >
          Login
        </RouterLink>
      </nav>
    </div>
  </header>
</template>
