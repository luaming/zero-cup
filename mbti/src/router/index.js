import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    {
        path: '/',
        name: 'Index',
        component: function () {
            return import('../views/Index.vue')
        }
    },
    {
        path: '/test',
        name: 'Test',
        component: function () {
            return import('../views/Test.vue')
        }
    },
    {
        path: '/Introduction',
        name: 'Introduction',
        component: function () {
            return import('../views/Introduction.vue')
        }
    },
    {
        path: '/Message',
        name: 'Message',
        component: function () {
            return import('../views/Message.vue')
        }
    },
    {
        path: '/Interaction',
        name: 'Interaction',
        component: function () {
            return import('../views/Interaction.vue')
        }
    },
    {
        path: '/Contact',
        name: 'contact',
        component: function () {
            return import('../views/Contact.vue')
        }
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
