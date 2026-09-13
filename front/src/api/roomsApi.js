import apiClient from "./apiClient";

const roomsApi = {
  async getRooms() {
    const response = await apiClient.get("/rooms");
    return response.data;
  },

  async getRoomById(id) {
    const response = await apiClient.get(`/rooms/${id}`);
    return response.data;
  },

  async createRoom(data) {
    const response = await apiClient.post("/rooms", data);
    return response.data;
  },

  // TODO: use after admin rooms edit UI is implemented
  async updateRoom(id, data) {
    const response = await apiClient.put(`/rooms/${id}`, data);
    return response.data;
  },

  async deleteRoom(id) {
    const response = await apiClient.delete(`/rooms/${id}`);
    return response.data;
  },
};

export default roomsApi;
