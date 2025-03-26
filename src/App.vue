<template>
  <div>
    <div class="px-5">
      <div class="row">
        <div class="col-md-3">
          <div class="card">
            <div class="card-body">
              <div class="d-flex align-items-center justify-content-between mb-3">
                <h5 class="card-title m-0">Todo</h5>
                <i class="fa-solid fa-ellipsis cursor p-2"></i>
              </div>
              <VueDraggable v-model="list">
                <div v-for="item in list" :key="item.id" class="card p-2 mb-3">
                  {{ item.name }}
                </div>
              </VueDraggable>
            </div>
          </div>
        </div>
      </div>
    </div>
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