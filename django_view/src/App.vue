<template>
  <nav class="navbar is-dark">
    <div class = 'navbar-brand'>
<router-link to="/" class="navbar-item">Home</router-link>
<router-link to = "/winter" class="navbar-item">Winter</router-link>
<div class="navbar-item">
  <div class="buttons">
    <router-link to="/logIn" class="button is-success">Login</router-link>
    <router-link to="/cart" class="button is-success">
      <span class="icon" ><i class="fas fa-shopping-cart"></i></span>
      <span>cart</span>
      </router-link>
  
  </div>
</div>
</div>
</nav>
  <section class = "section">
  <router-view/>
</section>
<footer class="footer">
<p class="has-text-centered">Jerry Dong</p>
</footer>


</template>
<script>

</script>

<style lang="scss">
@import '../node_modules/bulma'

</style>
