<template>
    <div>
      <h2>{{ currentQuestion.text }}</h2>
      <button @click="handleAnswer('yes')">Yes</button>
      <button @click="handleAnswer('no')">No</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        questions: {
          // Define your questions and follow-up questions in a nested structure
          1: { text: "Is the item made of paper?", next: { yes: 2, no: 3 } },
          2: { text: "Is the paper clean and unsoiled?", next: { yes: "recycle", no: "trash" } },
          3: { text: "Is the item made of glass?", next: { yes: 4, no: "trash" } },
          4: { text: "Is the glass container?", next: { yes: "recycle", no: "trash" } },
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
        alert(`You should ${result} this item.`);
        // Here you could also redirect the user or display additional information
      }
    }
  };
  </script>
  