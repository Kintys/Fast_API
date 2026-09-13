# Booking System — Project Progress

## Current Stage

Stage 12 (partial) — Add room form

## Completed

- [x] Stage 1 — Project setup
- [x] Stage 2 — Layout + Navbar
- [x] Stage 3 — API client
- [x] Stage 4 — roomsApi
- [x] Stage 5 — roomsStore
- [x] Stage 6 — RoomsView
- [x] Stage 7 — RoomCard
- [x] Stage 8 — Loading / Error / Empty states
- [x] Stage 9 — Room Details
- [x] Add room form (`/rooms/new`) via `POST /rooms`

## Next

- [ ] Stage 10 — Booking creation
- [ ] Stage 11 — My bookings
- [ ] Stage 12 — Admin rooms CRUD (edit remaining)
- [ ] Stage 13 — Admin bookings
- [ ] Stage 14 — Registration
- [ ] Stage 15 — Login
- [ ] Stage 16 — Authentication guards
- [ ] Stage 17 — Admin role guards

## Last Completed Work

- Added `/rooms/new` form page matching `RoomCreate` fields.
- Basic client validation for name, description, capacity, location, image URL.
- Sends data to `POST /api/rooms` through roomsStore → roomsApi.
- After success redirects to the new room details page.

## Important TODO

- Booking functionality is not implemented.
- Authentication is not implemented.
- Edit room UI is not implemented.
