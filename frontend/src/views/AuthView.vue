<script setup>
import { ref } from "vue";
import ErrorBanner from "@/components/ErrorBanner.vue";
import { register, login } from "@/utils/auth.js";
import { Notify } from "quasar";

const errors = ref([]);
const username = ref("");
const password = ref("");
const confirmPassword = ref("");
const showRegisterFields = ref(false);

const submit = async () => {
  if (showRegisterFields.value) {
    const response = await register(username, password, confirm);
    if (response.success != null) {
      Notify.create({
        message: "Registration successful",
        color: "positive",
        position: "top",
      });
      setTimeout(() => {
        window.location.href = "/templates";
      }, 1000);
    } else {
      console.log(response.errors);
      errors.value = response.errors;
    }
  } else {
    const response = await login(username, password, confirmPassword);
    if (response.success != null) {
      Notify.create({
        message: "Login successful",
        color: "positive",
        position: "top",
      });
      setTimeout(() => {
        window.location.href = "/subscriptions";
      }, 1000);
    } else {
      console.log(response.errors);
      errors.value = response.errors;
    }
  }
};
</script>

<template>
  <q-form class="" @submit="submit()">
    <div>
      <div class="q-ma-md">
        <q-card>
          <q-card-section class="text-center">
            <div class="text-h5">
              {{ !showRegisterFields ? "Login" : "Register" }}
            </div>
          </q-card-section>

          <q-card-section>
            <q-input
              v-model="username"
              label="Username"
              type="text"
              filled
              stack-label
              class="q-mb-md"
              lazy-rules
              :rules="[
                (val) => (val && val.length > 0) || 'Please type something',
              ]"
            />

            <q-input
              v-model="password"
              label="Password"
              type="password"
              filled
              stack-label
              class="q-mb-md"
              lazy-rules
              :rules="[
                (val) => (val && val.length > 0) || 'Please type something',
              ]"
            />

            <q-input
              v-model="confirmPassword"
              label="Confirm Password"
              type="password"
              filled
              stack-label
              class="q-mb-md"
              lazy-rules
              :rules="[
                (val) => (val && val.length > 0) || 'Please type something',
                (val) => val === password || 'Passwords do not match',
              ]"
              v-if="showRegisterFields"
            />
          </q-card-section>

          <ErrorBanner :errors="errors" />

          <q-card-section class="q-gutter-y-sm">
            <div class="text-center">
              <q-btn
                color="secondary"
                @click="showRegisterFields = !showRegisterFields"
                class="q-mr-md"
              >
                <q-icon
                  :name="
                    showRegisterFields
                      ? 'mdi-account-check'
                      : 'mdi-account-plus'
                  "
                  left
                />
                <div>{{ showRegisterFields ? "Login" : "Register" }}</div>
              </q-btn>
              <q-btn type="submit" color="primary">
                <q-icon
                  :name="
                    !showRegisterFields
                      ? 'mdi-account-check'
                      : 'mdi-account-plus'
                  "
                  left
                />
                <div>{{ !showRegisterFields ? "Login" : "Register" }}</div>
              </q-btn>
            </div>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-form>
</template>