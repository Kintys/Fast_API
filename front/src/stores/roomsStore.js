import { defineStore } from "pinia";
import roomsApi from "@/api/roomsApi";

export const useRoomsStore = defineStore("rooms", {
  state: () => ({
    rooms: [],
    loading: false,
    error: null,
    currentRoom: null,
    detailLoading: false,
    detailError: null,
    deletingId: null,
    creating: false,
    createError: null,
  }),

  actions: {
    async fetchRooms() {
      this.loading = true;
      this.error = null;

      try {
        this.rooms = await roomsApi.getRooms();
      } catch (error) {
        this.error = "Failed to load rooms";
      } finally {
        this.loading = false;
      }
    },

    async fetchRoomById(id) {
      this.detailLoading = true;
      this.detailError = null;
      this.currentRoom = null;

      try {
        this.currentRoom = await roomsApi.getRoomById(id);
      } catch (error) {
        this.detailError = "Failed to load room";
      } finally {
        this.detailLoading = false;
      }
    },

    async deleteRoom(id) {
      this.deletingId = id;

      try {
        await roomsApi.deleteRoom(id);
        this.rooms = this.rooms.filter((room) => room.id !== id);

        if (this.currentRoom?.id === id) {
          this.currentRoom = null;
        }

        return true;
      } catch (error) {
        return false;
      } finally {
        this.deletingId = null;
      }
    },

    async createRoom(data) {
      this.creating = true;
      this.createError = null;

      try {
        const createdRoom = await roomsApi.createRoom(data);
        this.rooms = [createdRoom, ...this.rooms];
        return createdRoom;
      } catch (error) {
        this.createError = "Failed to create room. Please try again.";
        return null;
      } finally {
        this.creating = false;
      }
    },
  },
});
