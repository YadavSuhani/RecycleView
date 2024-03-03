import Vue from 'vue';
import Router from 'vue-router';
import CheckObject from '@/views/check-object.vue';
import QuizTime from '@/views/quiz-time.vue';

Vue.use(Router);

export default new Router({
    mode: 'history',
    routes: [
    {
        path: '/',
        name: 'check-object',
        component: CheckObject
    },
    {
        path: '/',
        name: 'quiz-time',
        component: QuizTime
    }
    ]
});
