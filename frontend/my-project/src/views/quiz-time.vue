<template>
    <div>
        <h2>{{ currentQuestion.text }}</h2>

        <template v-if="currentQuestion.text === 'What material is your trash?'">
            <button class="home-button" @click="handleAnswer('glass')">Glass</button>
            <button class="home-button" @click="handleAnswer('metal')">Aluminum/Tin</button>
            <button class="home-button" @click="handleAnswer('pap')">Paper/Cardboard</button>
            <button class="home-button" @click="handleAnswer('plas')">Plastic</button>
        </template>

        <template v-else-if="currentQuestion.text === 'Is your item a cardboard box, shredded paper, or neither?'">
            <button class="home-button" @click="handleAnswer('box')">Cardboard Box</button>
            <button class="home-button" @click="handleAnswer('shr')">Shredded Paper</button>
            <button class="home-button" @click="handleAnswer('nth')">Neither</button>
        </template>

        <template v-else-if="currentQuestion.text === 'Which category best fits your object?'">
            <button class="home-button" @click="handleAnswer('film')">Bag, film, or styrofoam</button>
            <button class="home-button" @click="handleAnswer('bott')">Bottle, jug, or container</button>
        </template>

        <template v-else>
            <button class="home-button" @click="handleAnswer('yes')">Yes</button>
            <button class="home-button" @click="handleAnswer('no')">No</button>
        </template>

    </div>
</template>
  
  <script>
  export default {
    data() {
      return {
        questions: {
          // Define your questions and follow-up questions in a nested structure
          1: { text: "Is your item larger than a credit card?", next: { yes: 2, no: "small" } },

          2: { text: "What material is your trash?", next: { glass: "clean", metal: "clean" , pap: 3, plas: 4 } },

          3: { text: "Is your item a cardboard box, shredded paper, or neither?", next: { box: "card", shr: "bag", nth: "reg" } },

          4: { text: "Which category best fits your object?", next: { film: "nope", bott: 5 } },

          5: { text: "Is there a cap?", next: { yes: 6, no: "clean" } },

          6: { text: "Does the material of the cap match the material of the container?", next: { yes: "cap", no: "wrong" } },
          // Add additional questions as needed
        },
        currentQuestionId: 1, // Start with the first question
        path: [] // Keep track of the path of answers
      };
    },
    computed: {
      currentQuestion() {
        return this.questions[this.currentQuestionId];
      }
    },
    methods: {
      handleAnswer(answer) {
        const next = this.currentQuestion.next[answer];
  
        // Check if the next step is a question or a final action
        if (typeof next === 'number') {
          this.currentQuestionId = next;
        } else {
          this.finalAction(next); // 'next' would be "recycle" or "trash"
        }
  
        this.path.push({ question: this.currentQuestion.text, answer });
      },
      finalAction(result) {
        // Final action based on the result
        if (result === "small"){
            alert(`You cannot recycle it, it is too small to be processed`);
        } else if (result === "clean") {
            alert(`If it is clean, then it is good to recycle!`);
        } else if (result === "card"){
            alert(`If it is dry, clean, and broken down, then it is good to recycle!`);
        } else if (result === "bag"){
            alert(`Place the shreds into a paper bag, then you are good to recycle it!`);
        } else if (result === "reg"){
            alert(`If it is dry and clean, then it is good to recycle!`);
        } else if (result === "cap"){
            alert(`If it is clean, then it is good to recycle with the cap!`);
        } else if (result === "wrong"){
            alert(`Remove the cap first and throw it out, it cannot be recycled. If the container itself is clean, you are good to recycle it!`);
        } 
        
        // Here you could also redirect the user or display additional information
      }
    }
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
  margin-right: 7px;
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