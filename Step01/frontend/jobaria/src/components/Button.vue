<template>
  <button :value="value">{{ text }}</button>
</template>

<script>
export default {
  name: "Button",
  props: {
    text: String,
    value: Number
  },
};
</script>

<style lang="scss" scoped>
button {
  padding: 1em;
  margin: 1em;
  background-color: #2dad67;
  cursor: pointer;
  outline: none;
  border: 2px solid #2dad67;
  border-radius: 2em;
  color: white;
  font-weight: bold;
  &:hover {
    background-color: white;
    border: 2px dashed #2dad67;
    color: #2dad67;
    transition: background-color 0.3s ease;
  }
}
</style>
