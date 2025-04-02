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
              <VueDraggable @add="moveTodo($event, column.id)" v-model="column.todos" animation="150" ghostClass="ghost" group="people">
                <div v-for="item in column.todos" :key="item.id" class="card p-2 mb-3 coolhoverpedrito">
                  <span v-if="!item.editing" @dblclick="enableEdit(item)">
                    {{ item.name }}
                  </span>
                  <input v-else v-focus type="text" v-model="item.name" @blur="disableEdit(item)" @keyup.enter="disableEdit(item)" style="z-index: 9;" />
                  <button @click="deleteTodo(item.id)" class="btn btn-light p-1 py-0 supertacha"><i class="fa-solid fa-xmark"></i></button>
                </div>
              </VueDraggable>
              <button @click="addTodo(column.id)" type="button" class="btn btn-light"><i class="fa-solid fa-plus me-1"></i> Agregar nueva tarea</button>
            </div>
          </div>
        </div>


      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { VueDraggable } from 'vue-draggable-plus'

export default {
  components: {
    VueDraggable
  },
  async mounted(){
    const result = await axios.get("/api/columns/")
    this.columns = result.data
  },
  data() {
    return {
      temporaryFinalId: 99,
      columns: []
    }
  },
  methods: {
    async addTodo(columnId) {
      const newTodo = { name: "Tarea Nueva", idColumn: columnId }
      const result = await axios.post("/api/todos/", newTodo)
      const column = this.columns.find(x => x.id === columnId)
      if (column) {
        column.todos.push(result.data)
      }
    },
    enableEdit(item) {
      this.$set(item, 'editing', true)
    },
    async disableEdit(item) {
      item.editing = false;
      await axios.put(`/api/todos/${item.id}/`, item)
    },
    async moveTodo(event, columnId) {
      this.$nextTick(async () => {
        const todo = this.columns.flatMap(x => x.todos).find(y => y.id === event.data.id)
        if (todo) {
          todo.idColumn = columnId
        }
        await axios.put(`/api/todos/${todo.id}/`, todo)
      });
    },
    async deleteTodo(todoId) {
      await axios.delete(`/api/todos/${todoId}/`)
      const column = this.columns.find(x => x.todos.find(y => y.id === todoId));
      if (column) {
        column.todos = column.todos.filter(x => x.id !== todoId);
      }
    }
  }
}
</script>


<style>
.coolhoverpedrito {
  position: relative;
}

.coolhoverpedrito:hover .supertacha {
  visibility: visible;
  z-index: 4;
  opacity: 0.2;
}

.supertacha {
  position: absolute;
  right: 10px;
  visibility: hidden;
}

.ghost {
  opacity: 0.2;
}
</style>