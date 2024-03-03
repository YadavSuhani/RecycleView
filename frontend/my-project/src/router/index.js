import { createRouter, createWebHistory } from 'vue-router';
import CheckObject from '@/views/check-object.vue';
import QuizTime from '@/views/quiz-time.vue';
import App from '@/App.vue';


const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      //name: 'check-object',
      component: App,
    },
    {
        path : '/check-object',
        component: CheckObject,
    },
    {
      path: '/quiz-time',
      //name: 'quiz-time',
      component: QuizTime,
    },
  ],
});

export default router;

