/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./**/templates/**/*.html",
    "./templates/*.html",
  ],
  darkMode: 'class', // 👈 이 줄을 반드시 추가해야 버튼이 작동합니다!
  theme: {
    extend: {},
  },
  plugins: [],
}
