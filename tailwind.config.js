/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './main/templates/main/*.html',
    './users/templates/users/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
