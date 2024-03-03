import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import CheckObject from '@/views/check-object.vue';
import QuizTime from '@/views/quiz-time.vue';
import HomePage from '@/views/home-page.vue';
import App from '@/App.vue';

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'home-page',
            component: HomePage
        },
        {
            path: '/check-object',
            name: 'check-object',
            component: CheckObject
        },
        {
          path: '/quiz-time',
          name: 'quiz-time',
          component: QuizTime
        },
    ]
})

const app = createApp(App)
app.use(router);
app.mount('#app')