<script setup>
import { RouterLink } from "vue-router";
import { storeToRefs } from "pinia";
import { useRoomsStore } from "@/stores/roomsStore";

const props = defineProps({
  room: {
    type: Object,
    required: true,
  },
});

const roomsStore = useRoomsStore();
const { deletingId } = storeToRefs(roomsStore);

async function onDelete() {
  const confirmed = window.confirm(
    `Delete room "${props.room.name}"? This cannot be undone.`
  );

  if (!confirmed) {
    return;
  }

  const deleted = await roomsStore.deleteRoom(props.room.id);

  if (!deleted) {
    window.alert("Failed to delete room. Please try again.");
  }
}
</script>

<template>
  <article
    class="flex h-full flex-col overflow-hidden rounded-lg border border-slate-200 bg-white shadow-sm transition"
    :class="room.isActive ? 'opacity-100' : 'opacity-70'"
  >
    <div class="aspect-[16/10] overflow-hidden bg-slate-100">
      <img
        v-if="room.imageUrl"
        :src="room.imageUrl"
        :alt="room.name"
        class="h-full w-full object-cover"
      />
      <div
        v-else
        class="flex h-full w-full items-center justify-center text-sm text-slate-400"
      >
        No photo
      </div>
    </div>

    <div class="flex flex-1 flex-col p-5">
      <div class="mb-3 flex items-start justify-between gap-3">
        <h2 class="text-lg font-semibold text-slate-900">
          {{ room.name }}
        </h2>
        <span
          class="shrink-0 rounded-md px-2 py-1 text-xs font-medium"
          :class="
            room.isActive
              ? 'bg-green-100 text-green-800'
              : 'bg-slate-200 text-slate-600'
          "
        >
          {{ room.isActive ? "Active" : "Inactive" }}
        </span>
      </div>

      <p class="mb-4 line-clamp-2 flex-1 text-sm text-slate-600">
        {{ room.description }}
      </p>

      <dl class="mb-5 space-y-2 text-sm text-slate-700">
        <div class="flex items-center gap-2">
          <svg
            class="h-4 w-4 shrink-0 text-slate-400"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            stroke-width="1.5"
            aria-hidden="true"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M15 19.128a9.38 9.38 0 002.625.372 9.337 9.337 0 004.121-.952 4.125 4.125 0 00-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 018.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0111.964-3.07M12 6.375a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zm8.25 2.25a2.625 2.625 0 11-5.25 0 2.625 2.625 0 015.25 0z"
            />
          </svg>
          <dt class="sr-only">Capacity</dt>
          <dd>Capacity: {{ room.capacity }}</dd>
        </div>
        <div class="flex items-center gap-2">
          <svg
            class="h-4 w-4 shrink-0 text-slate-400"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            stroke-width="1.5"
            aria-hidden="true"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z"
            />
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z"
            />
          </svg>
          <dt class="sr-only">Location</dt>
          <dd>{{ room.location }}</dd>
        </div>
      </dl>

      <div class="mt-auto flex gap-2">
        <RouterLink
          :to="`/rooms/${room.id}`"
          class="inline-flex flex-1 items-center justify-center rounded-md border border-slate-300 bg-white px-3 py-2 text-sm font-medium text-slate-800 transition hover:bg-slate-50"
        >
          View room
        </RouterLink>
        <button
          type="button"
          class="inline-flex items-center justify-center rounded-md border border-red-200 bg-white px-3 py-2 text-sm font-medium text-red-700 transition hover:bg-red-50 disabled:cursor-not-allowed disabled:opacity-60"
          :disabled="deletingId === room.id"
          @click="onDelete"
        >
          {{ deletingId === room.id ? "Deleting..." : "Delete" }}
        </button>
      </div>
    </div>
  </article>
</template>
