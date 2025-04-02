import Vue from 'vue'
import App from './App.vue'
import axios from 'axios';


axios.defaults.baseURL = window.location.origin

Vue.directive('focus', {
  inserted(el) {
    el.focus();
  }
})

new Vue({
  render: (h) => h(App)
}).$mount('#app')
