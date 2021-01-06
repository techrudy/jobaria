import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/login/candidate",
    name: "CandidateLogin",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        /* webpackChunkName: "candidatelogin" */ `../views/auth/login/CandidateLogin.vue`
      )
  },
  {
    path: "/login/professional",
    name: "ProfessionalLogin",
    component: () =>
      import(
        /* webpackChunkName: "professionallogin" */ `../views/auth/login/ProfessionalLogin.vue`
      )
  },
  {
    path: "/register/candidate",
    name: "CandidateRegister",
    component: () =>
      import(
        /* webpackChunkName: "candidateregister" */ `../views/auth/register/CandidateRegister.vue`
      )
  },
  {
    path: "/register/professional",
    name: "ProfessionalRegister",
    component: () =>
      import(
        /* webpackChunkName: "professionalregister" */ `../views/auth/register/ProfessionalRegister.vue`
      )
  },
  {
    path: "/profile",
    name: "UserProfile",
    component: () =>
      import(
        /* webpackChunkName: "userprofile" */ `../views/profile/UserProfile.vue`
      )
  },
  {
    path: "/myjoboffers",
    name: "GetMyJobOffers",
    component: () =>
      import(
        /* webpackChunkName: "getmyjoboffers" */ `../views/joboffers/GetMyJobOffers.vue`
      )
  },
  {
    path: "/myjoboffers/create",
    name: "CreateJobOffer",
    component: () =>
      import(
        /* webpackChunkName: "createjoboffer" */ `../views/joboffers/CreateJobOffer.vue`
      )
  },
  {
    path: "/myjoboffers/edit/:id",
    name: "EditJobOffer",
    props: true,
    component: () =>
      import(
        /* webpackChunkName: "editjoboffer" */ `../views/joboffers/EditJobOffer.vue`
      )
  },
  {
    path: "/404",
    name: "NotFound",
    component: () =>
      import(
        /* webpackChunkName: "notfound" */ `../views/NotFound.vue`
      )
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

router.beforeEach((to, from, next) => {
  if (!to.matched.length) {
    next('/404');
  } else {
    next();
  }
})

export default router;
