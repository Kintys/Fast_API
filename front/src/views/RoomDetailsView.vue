<script setup>
import { watch } from "vue";
import { useRoute, useRouter, RouterLink } from "vue-router";
import { storeToRefs } from "pinia";
import { useRoomsStore } from "@/stores/roomsStore";
import AppContainer from "@/components/layout/AppContainer.vue";

const route = useRoute();
const router = useRouter();
const roomsStore = useRoomsStore();
const { currentRoom, detailLoading, detailError, deletingId } =
  storeToRefs(roomsStore);

// TODO: add booking form
// TODO: add room availability check

watch(
  () => route.params.id,
  (id) => {
    if (id) {
      roomsStore.fetchRoomById(id);
    }
  },
  { immediate: true }
);

async function onDelete() {
  if (!currentRoom.value) {
    return;
  }

  const confirmed = window.confirm(
    `Delete room "${currentRoom.value.name}"? This cannot be undone.`
  );

  if (!confirmed) {
    return;
  }

  const deleted = await roomsStore.deleteRoom(currentRoom.value.id);

  if (deleted) {
    router.push("/rooms");
  } else {
    window.alert("Failed to delete room. Please try again.");
  }
}
</script>

<template>
  <AppContainer>
    <div class="mb-6">
      <RouterLink
        to="/rooms"
        class="text-sm font-medium text-slate-600 transition hover:text-slate-900"
      >
        Back to rooms
      </RouterLink>
    </div>

    <!-- Loading -->
    <div
      v-if="detailLoading"
      class="animate-pulse overflow-hidden rounded-lg border border-slate-200 bg-white"
    >
      <div class="aspect-[21/9] bg-slate-200" />
      <div class="space-y-4 p-6">
        <div class="h-8 w-1/2 rounded bg-slate-200" />
        <div class="h-4 w-full rounded bg-slate-200" />
        <div class="h-4 w-2/3 rounded bg-slate-200" />
      </div>
    </div>

    <!-- Error -->
    <div
      v-else-if="detailError"
      class="rounded-lg border border-red-200 bg-red-50 px-6 py-10 text-center"
    >
      <p class="text-base font-medium text-red-800">Unable to load room.</p>
      <p class="mt-1 text-sm text-red-700">Please try again.</p>
      <button
        type="button"
        class="mt-5 inline-flex rounded-md bg-slate-900 px-4 py-2 text-sm font-medium text-white transition hover:bg-slate-800"
        @click="roomsStore.fetchRoomById(route.params.id)"
      >
        Retry
      </button>
    </div>

    <!-- Room details -->
    <article
      v-else-if="currentRoom"
      class="overflow-hidden rounded-lg border border-slate-200 bg-white shadow-sm"
    >
      <div class="aspect-[21/9] bg-slate-100 sm:aspect-[2/1]">
        <img
          v-if="currentRoom.imageUrl"
          :src="currentRoom.imageUrl"
          :alt="currentRoom.name"
          class="h-full w-full object-cover"
        />
        <div
          v-else
          class="flex h-full w-full items-center justify-center text-slate-400"
        >
          No photo
        </div>
      </div>

      <div class="p-6 sm:p-8">
        <div class="flex flex-wrap items-start justify-between gap-4">
          <div>
            <h1 class="text-2xl font-semibold tracking-tight text-slate-900 sm:text-3xl">
              {{ currentRoom.name }}
            </h1>
            <p class="mt-2 text-slate-600">
              {{ currentRoom.description }}
            </p>
          </div>
          <span
            class="rounded-md px-2.5 py-1 text-xs font-medium"
            :class="
              currentRoom.isActive
                ? 'bg-green-100 text-green-800'
                : 'bg-slate-200 text-slate-600'
            "
          >
            {{ currentRoom.isActive ? "Active" : "Inactive" }}
          </span>
        </div>

        <dl class="mt-8 grid gap-4 sm:grid-cols-2">
          <div class="rounded-md border border-slate-100 bg-slate-50 px-4 py-3">
            <dt class="text-xs font-medium uppercase tracking-wide text-slate-500">
              Capacity
            </dt>
            <dd class="mt-1 text-base text-slate-900">
              {{ currentRoom.capacity }} people
            </dd>
          </div>
          <div class="rounded-md border border-slate-100 bg-slate-50 px-4 py-3">
            <dt class="text-xs font-medium uppercase tracking-wide text-slate-500">
              Location
            </dt>
            <dd class="mt-1 text-base text-slate-900">
              {{ currentRoom.location }}
            </dd>
          </div>
          <div class="rounded-md border border-slate-100 bg-slate-50 px-4 py-3">
            <dt class="text-xs font-medium uppercase tracking-wide text-slate-500">
              Room ID
            </dt>
            <dd class="mt-1 text-base text-slate-900">
              {{ currentRoom.id }}
            </dd>
          </div>
          <div class="rounded-md border border-slate-100 bg-slate-50 px-4 py-3">
            <dt class="text-xs font-medium uppercase tracking-wide text-slate-500">
              Status
            </dt>
            <dd class="mt-1 text-base text-slate-900">
              {{ currentRoom.isActive ? "Active" : "Inactive" }}
            </dd>
          </div>
        </dl>

        <p
          v-if="!currentRoom.isActive"
          class="mt-6 rounded-md border border-amber-200 bg-amber-50 px-4 py-3 text-sm text-amber-800"
        >
          This room is inactive and cannot be booked.
        </p>

        <div class="mt-8 flex flex-wrap gap-3">
          <button
            type="button"
            class="inline-flex rounded-md border border-red-200 bg-white px-4 py-2 text-sm font-medium text-red-700 transition hover:bg-red-50 disabled:cursor-not-allowed disabled:opacity-60"
            :disabled="deletingId === currentRoom.id"
            @click="onDelete"
          >
            {{ deletingId === currentRoom.id ? "Deleting..." : "Delete room" }}
          </button>
          <p class="w-full text-sm text-slate-500">
            Booking functionality coming soon.
          </p>
        </div>
      </div>
    </article>
  </AppContainer>
</template>
