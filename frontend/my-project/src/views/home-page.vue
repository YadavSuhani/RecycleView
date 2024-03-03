<template>
    <div>
        <h1>
            Welcome to RecycleView!
        </h1>
        <h3>
            yup! we've all been there! (hush...)
        </h3>
        <div>
            <button class="home-button" @click="$router.push('/check-object')">
                pretend to take a photo of the piece of trash in front of you
            </button>
        </div>
        <div>
            <button class="home-button" @click="$router.push('/quiz-time')">
                i'd like to learn, actually
            </button>
        </div>
    </div>
</template>

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
</style>