import { createRouter, createWebHistory } from 'vue-router'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: () => import('@/views/auth/Login.vue')
    },{
      path: '/hr',
      component: () => import('@/components/Layout/Hr.vue'),
      children: [
        {
          path: "",
          name: "hr-dashboard",
          component: () => import("@/views/hr/Dashboard.vue")
        }
      ]
    }
  ],
})

export default router
