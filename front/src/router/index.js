import { createRouter, createWebHistory } from "vue-router";

import HomeView from "@/views/HomeView.vue";
import RoomsView from "@/views/RoomsView.vue";
import AddRoomView from "@/views/AddRoomView.vue";
import RoomDetailsView from "@/views/RoomDetailsView.vue";
import MyBookingsView from "@/views/MyBookingsView.vue";
import LoginView from "@/views/LoginView.vue";
import RegisterView from "@/views/RegisterView.vue";
import AdminRoomsView from "@/views/admin/AdminRoomsView.vue";
import AdminBookingsView from "@/views/admin/AdminBookingsView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/rooms",
      name: "rooms",
      component: RoomsView,
    },
    {
      path: "/rooms/new",
      name: "add-room",
      component: AddRoomView,
    },
    {
      path: "/rooms/:id",
      name: "room-details",
      component: RoomDetailsView,
    },
    {
      path: "/my-bookings",
      name: "my-bookings",
      component: MyBookingsView,
    },
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    {
      path: "/register",
      name: "register",
      component: RegisterView,
    },
    {
      path: "/admin/rooms",
      name: "admin-rooms",
      component: AdminRoomsView,
    },
    {
      path: "/admin/bookings",
      name: "admin-bookings",
      component: AdminBookingsView,
    },
  ],
});

// TODO: add authentication and role guards

export default router;
