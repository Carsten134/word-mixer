<script setup lang="ts">
    const percent = ref(50)
    const left = ref("left")
    const right = ref("right")

    const output = ref("")
    async function fetchCandidates() {
        output.value = await $fetch(`http://127.0.0.1:5000/word2vec/perfect-match?left=${left.value}&right=${right.value}&percent=${percent.value/100}`)
    }

    output.value = [["test"],["test2"]]
</script>

<template>
  <div class="h-screen v-screen flex flex-col justify-center items-center">
    <span class="text-3xl font-bold font-serif">Word Mixer</span>
    <p class="mb-4">Enter your scale and words to get suggestions</p>
    <div class="flex flex-col justify-center items-center broder-solid border-[1px] border-slate-200 rounded-md shadow-xl p-4">
      <div class="mb-5">
        <input type="text" v-model="left" class="w-16 mr-5 transition-all ease-in ease-outk"/>
        <input type="range" v-model="percent" class=""/>
        <input type="text" v-model="right" class="w-16 ml-5 transition-all ease-in ease-out">
      </div>
      <button @click="fetchCandidates" class="px-3 py-1 broder-solid border-[1px] rounded-full hover:shadow-md transition-all ease-in ease-out">Send</button> <br>
    </div>
   
    <ol class="mt-10 list-decimal space-y-1 text-gray-500">
        <li v-for="item in output"><span class="font-bold text-1xl text-black">{{ item[0] }}</span></li>
    </ol>
  </div>
</template>
