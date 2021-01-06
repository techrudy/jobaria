<template>
  <div class="footer">
      <div class="footer__text">
          <p>Jobaria est un site d'offre d'emploi</p>
      </div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="scss" scoped>
.footer {
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 10em;
    display: flex;
    justify-content: center;
    align-content: center;
    align-items: center;
    background-color: #2dad67;
    &__text {
        color: white;
        font-weight: bold;
        font-size: 16px;
    }
}
</style>