<template>
  <div>
    <h1>This is {{ message }}</h1>
    <VueDraggable v-model="list">
      <div v-for="item in list" :key="item.id">
        {{ item.name }}
      </div>
    </VueDraggable>
  </div>
</template>



<script>
import { VueDraggable } from 'vue-draggable-plus'
export default {
  components: {
    VueDraggable
  },
  data() {
    return {
      message: "vue view",
      list: [
        {
          name: 'Joao',
          id: 1
        },
        {
          name: 'Jean',
          id: 2
        },
        {
          name: 'Johanna',
          id: 3
        },
        {
          name: 'Juan',
          id: 4
        }
      ]
    }
  }
}
</script>