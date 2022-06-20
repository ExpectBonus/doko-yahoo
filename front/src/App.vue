<template>
  <ProfileView> </ProfileView>
</template>

<script>
import ProfileView from "./views/ProfileView.vue";

export default {
  name: "App",
  components: {
    ProfileView,
  },
  data: function () {
    return {
      name: "guest",
    };
  },
};
</script>
