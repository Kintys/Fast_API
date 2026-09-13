<script setup>
import { onMounted } from "vue";
import { RouterLink } from "vue-router";
import { storeToRefs } from "pinia";
import { useRoomsStore } from "@/stores/roomsStore";
import AppContainer from "@/components/layout/AppContainer.vue";
import RoomCard from "@/components/rooms/RoomCard.vue";

const roomsStore = useRoomsStore();
const { rooms, loading, error } = storeToRefs(roomsStore);

onMounted(() => {
  roomsStore.fetchRooms();
});
</script>

<template>
  <AppContainer>
    <div class="mb-8 flex flex-wrap items-start justify-between gap-4">
      <div>
        <h1 class="text-2xl font-semibold tracking-tight text-slate-900 sm:text-3xl">
          Rooms
        </h1>
        <p class="mt-2 text-slate-600">
          Find a room for your meeting or event.
        </p>
      </div>
      <RouterLink
        to="/rooms/new"
        class="inline-flex rounded-md bg-slate-900 px-4 py-2 text-sm font-medium text-white transition hover:bg-slate-800"
      >
        Add room
      </RouterLink>
    </div>

    <!-- Loading state -->
    <div
      v-if="loading"
      class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3"
    >
      <div
        v-for="n in 6"
        :key="n"
        class="animate-pulse rounded-lg border border-slate-200 bg-white p-5"
      >
        <div class="mb-4 flex items-start justify-between">
          <div class="h-5 w-2/3 rounded bg-slate-200" />
          <div class="h-5 w-16 rounded bg-slate-200" />
        </div>
        <div class="mb-2 h-4 w-full rounded bg-slate-200" />
        <div class="mb-6 h-4 w-4/5 rounded bg-slate-200" />
        <div class="mb-2 h-4 w-1/3 rounded bg-slate-200" />
        <div class="mb-6 h-4 w-1/2 rounded bg-slate-200" />
        <div class="h-9 w-full rounded bg-slate-200" />
      </div>
    </div>

    <!-- Error state -->
    <div
      v-else-if="error"
      class="rounded-lg border border-red-200 bg-red-50 px-6 py-10 text-center"
    >
      <p class="text-base font-medium text-red-800">Unable to load rooms.</p>
      <p class="mt-1 text-sm text-red-700">Please try again.</p>
      <button
        type="button"
        class="mt-5 inline-flex rounded-md bg-slate-900 px-4 py-2 text-sm font-medium text-white transition hover:bg-slate-800"
        @click="roomsStore.fetchRooms()"
      >
        Retry
      </button>
    </div>

    <!-- Empty state -->
    <div
      v-else-if="rooms.length === 0"
      class="rounded-lg border border-slate-200 bg-white px-6 py-10 text-center"
    >
      <p class="text-base text-slate-600">No rooms available.</p>
    </div>

    <!-- Rooms grid -->
    <div
      v-else
      class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3"
    >
      <RoomCard v-for="room in rooms" :key="room.id" :room="room" />
    </div>
  </AppContainer>
</template>
