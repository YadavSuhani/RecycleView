<template>
    <div>
      <h2>Okay, what do we have here...</h2>
      <input ref="file" type="file" hidden @change="previewImage">
      <div class="button-container">
        <button class="home-button" @click="chooseFiles()">Upload Picture</button>
      </div>
      <div class="image-container" v-if="imageUrl">
        <img :src="imageUrl" alt="Uploaded Image" class="uploaded-image">
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        imageUrl: null,
      };
    },
    methods: {
      chooseFiles() {
        this.$refs.file.click();
      },
      previewImage(event) {
        const file = event.target.files[0];
        if (file) {
          this.imageUrl = URL.createObjectURL(file);
        }
      },
    },
  };
  </script>
  

<style>
.home-button {
  background-color: #2dfe54;
  border: 2px solid #422800;
  border-radius: 30px;
  box-shadow: #422800 4px 4px 0 0;
  color: #422800;
  cursor: pointer;
  display: inline-block;
  font-weight: 600;
  font-size: 18px;
  padding: 0 18px;
  line-height: 50px;
  text-align: center;
  text-decoration: none;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  margin-bottom: 10px;
}

.home-button:hover {
  background-color: #fff;
}

.home-button:active {
  box-shadow: #422800 2px 2px 0 0;
  transform: translate(2px, 2px);
}

@media (min-width: 768px) {
  .home-button {
    min-width: 120px;
    padding: 0 25px;
  }
}

.image-container {
  margin-top: 10px; 
}

.uploaded-image {
  max-width: 100%; 
  height: auto;
}
</style>