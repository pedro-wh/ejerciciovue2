<template>
  <div>
    <div class="px-5">
      <div class="row">


        <div class="col-md-3" v-for="column in columns">
          <div class="card">
            <div class="card-body">
              <div class="d-flex align-items-center justify-content-between mb-3">
                <h5 class="card-title m-0">Todo</h5>
                <i class="fa-solid fa-ellipsis cursor p-2"></i>
              </div>
              <VueDraggable v-model="column.todos" animation="150" ghostClass="ghost" group="people">
                <div v-for="item in column.todos" :key="item.id" class="card p-2 mb-3">
                  {{ item.name }}
                </div>
              </VueDraggable>
              <button @click="addTodo(column.id)" type="button" class="btn btn-light"><i class="fa-solid fa-plus me-1"></i> Agregar nueva tarea </button>
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
      temporaryFinalId: 99,
      columns: [
        {
          id: 1,
          todos: [
            {
              id: 8,
              name: "Tarea 1"
            },
            {
              id: 9,
              name: "Tarea 2"
            }
          ]
        },
        {
          id: 2,
          todos: [
            {
              id: 10,
              name: "Tarea 3",
            }
          ]
        }
      ]
    }
  },
  methods: {
    addTodo(columnId){
      const newTodo = {id: 99, name: "Tarea Nueva"}
      const column = this.columns.find(x => x.id === columnId)
      if(column){
        column.todos.push(newTodo)
      }
    }
  }
}
</script>