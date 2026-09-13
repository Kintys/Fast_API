<script setup>
import { reactive, ref, computed } from "vue";
import { useRouter, RouterLink } from "vue-router";
import { storeToRefs } from "pinia";
import { useRoomsStore } from "@/stores/roomsStore";
import AppContainer from "@/components/layout/AppContainer.vue";

const router = useRouter();
const roomsStore = useRoomsStore();
const { creating, createError } = storeToRefs(roomsStore);

const form = reactive({
  name: "",
  description: "",
  capacity: 1,
  location: "",
  isActive: true,
  imageUrl: "",
});

const errors = reactive({
  name: "",
  description: "",
  capacity: "",
  location: "",
  imageUrl: "",
});

const submitted = ref(false);

const imagePreviewUrl = computed(() => {
  const url = form.imageUrl.trim();
  if (!url) {
    return "";
  }

  try {
    const parsed = new URL(url);
    if (parsed.protocol !== "http:" && parsed.protocol !== "https:") {
      return "";
    }
    return url;
  } catch {
    return "";
  }
});

function isValidHttpUrl(value) {
  try {
    const parsed = new URL(value);
    return parsed.protocol === "http:" || parsed.protocol === "https:";
  } catch {
    return false;
  }
}

function validate() {
  let isValid = true;

  errors.name = "";
  errors.description = "";
  errors.capacity = "";
  errors.location = "";
  errors.imageUrl = "";

  if (!form.name.trim()) {
    errors.name = "Name is required.";
    isValid = false;
  } else if (form.name.trim().length < 2) {
    errors.name = "Name must be at least 2 characters.";
    isValid = false;
  }

  if (!form.description.trim()) {
    errors.description = "Description is required.";
    isValid = false;
  } else if (form.description.trim().length < 5) {
    errors.description = "Description must be at least 5 characters.";
    isValid = false;
  }

  const capacity = Number(form.capacity);
  if (!Number.isInteger(capacity) || capacity < 1) {
    errors.capacity = "Capacity must be a whole number of at least 1.";
    isValid = false;
  } else if (capacity > 500) {
    errors.capacity = "Capacity cannot be greater than 500.";
    isValid = false;
  }

  if (!form.location.trim()) {
    errors.location = "Location is required.";
    isValid = false;
  }

  if (form.imageUrl.trim() && !isValidHttpUrl(form.imageUrl.trim())) {
    errors.imageUrl = "Image must be a valid http or https URL.";
    isValid = false;
  }

  return isValid;
}

async function onSubmit() {
  submitted.value = true;

  if (!validate()) {
    return;
  }

  const payload = {
    name: form.name.trim(),
    description: form.description.trim(),
    capacity: Number(form.capacity),
    location: form.location.trim(),
    isActive: Boolean(form.isActive),
    imageUrl: form.imageUrl.trim() || null,
  };

  const createdRoom = await roomsStore.createRoom(payload);

  if (createdRoom) {
    router.push(`/rooms/${createdRoom.id}`);
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

    <div class="mb-8 max-w-2xl">
      <h1 class="text-2xl font-semibold tracking-tight text-slate-900 sm:text-3xl">
        Add room
      </h1>
      <p class="mt-2 text-slate-600">
        Create a new room. Image should be a public photo URL.
      </p>
    </div>

    <form
      class="max-w-2xl space-y-5 rounded-lg border border-slate-200 bg-white p-6 shadow-sm"
      @submit.prevent="onSubmit"
    >
      <div>
        <label for="name" class="mb-1.5 block text-sm font-medium text-slate-700">
          Name
        </label>
        <input
          id="name"
          v-model="form.name"
          type="text"
          class="w-full rounded-md border border-slate-300 px-3 py-2 text-sm text-slate-900 outline-none transition focus:border-slate-500 focus:ring-1 focus:ring-slate-500"
          placeholder="Conference Room A"
        />
        <p v-if="submitted && errors.name" class="mt-1 text-sm text-red-600">
          {{ errors.name }}
        </p>
      </div>

      <div>
        <label
          for="description"
          class="mb-1.5 block text-sm font-medium text-slate-700"
        >
          Description
        </label>
        <textarea
          id="description"
          v-model="form.description"
          rows="3"
          class="w-full rounded-md border border-slate-300 px-3 py-2 text-sm text-slate-900 outline-none transition focus:border-slate-500 focus:ring-1 focus:ring-slate-500"
          placeholder="Meeting room for small teams"
        />
        <p
          v-if="submitted && errors.description"
          class="mt-1 text-sm text-red-600"
        >
          {{ errors.description }}
        </p>
      </div>

      <div class="grid gap-5 sm:grid-cols-2">
        <div>
          <label
            for="capacity"
            class="mb-1.5 block text-sm font-medium text-slate-700"
          >
            Capacity
          </label>
          <input
            id="capacity"
            v-model.number="form.capacity"
            type="number"
            min="1"
            max="500"
            class="w-full rounded-md border border-slate-300 px-3 py-2 text-sm text-slate-900 outline-none transition focus:border-slate-500 focus:ring-1 focus:ring-slate-500"
          />
          <p
            v-if="submitted && errors.capacity"
            class="mt-1 text-sm text-red-600"
          >
            {{ errors.capacity }}
          </p>
        </div>

        <div>
          <label
            for="location"
            class="mb-1.5 block text-sm font-medium text-slate-700"
          >
            Location
          </label>
          <input
            id="location"
            v-model="form.location"
            type="text"
            class="w-full rounded-md border border-slate-300 px-3 py-2 text-sm text-slate-900 outline-none transition focus:border-slate-500 focus:ring-1 focus:ring-slate-500"
            placeholder="Floor 2 / Room 205"
          />
          <p
            v-if="submitted && errors.location"
            class="mt-1 text-sm text-red-600"
          >
            {{ errors.location }}
          </p>
        </div>
      </div>

      <div>
        <label
          for="imageUrl"
          class="mb-1.5 block text-sm font-medium text-slate-700"
        >
          Photo URL
          <span class="font-normal text-slate-500">(optional)</span>
        </label>
        <input
          id="imageUrl"
          v-model="form.imageUrl"
          type="url"
          class="w-full rounded-md border border-slate-300 px-3 py-2 text-sm text-slate-900 outline-none transition focus:border-slate-500 focus:ring-1 focus:ring-slate-500"
          placeholder="https://images.unsplash.com/..."
        />
        <p
          v-if="submitted && errors.imageUrl"
          class="mt-1 text-sm text-red-600"
        >
          {{ errors.imageUrl }}
        </p>

        <div
          v-if="imagePreviewUrl"
          class="mt-3 overflow-hidden rounded-md border border-slate-200 bg-slate-50"
        >
          <img
            :src="imagePreviewUrl"
            alt="Room photo preview"
            class="max-h-48 w-full object-cover"
          />
        </div>
      </div>

      <div class="flex items-center gap-2">
        <input
          id="isActive"
          v-model="form.isActive"
          type="checkbox"
          class="h-4 w-4 rounded border-slate-300 text-slate-900 focus:ring-slate-500"
        />
        <label for="isActive" class="text-sm text-slate-700">
          Room is active
        </label>
      </div>

      <div
        v-if="createError"
        class="rounded-md border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700"
      >
        {{ createError }}
      </div>

      <div class="flex flex-wrap gap-3 pt-2">
        <button
          type="submit"
          class="inline-flex rounded-md bg-slate-900 px-4 py-2 text-sm font-medium text-white transition hover:bg-slate-800 disabled:cursor-not-allowed disabled:opacity-60"
          :disabled="creating"
        >
          {{ creating ? "Creating..." : "Create room" }}
        </button>
        <RouterLink
          to="/rooms"
          class="inline-flex rounded-md border border-slate-300 bg-white px-4 py-2 text-sm font-medium text-slate-800 transition hover:bg-slate-50"
        >
          Cancel
        </RouterLink>
      </div>
    </form>
  </AppContainer>
</template>
