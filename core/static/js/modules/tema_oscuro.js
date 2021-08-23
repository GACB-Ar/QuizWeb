const d = document,
  ls = localStorage;

export default function darkTheme(btn, classDark) {
  const $themeBtn = d.querySelector(btn),
    $selectors = d.querySelectorAll('[data-dark]');
  // busca los elementos con ese atributo custom
  // console.log($selectors);
  let moon = '🌙',
    sun = '☀️';

  /* LocalStorage puede almacenar mayor cantidad de información y realizar muchas operaciones adicionales a la de una cookie, además es mucho más seguro que utilizar cookies.
  Se puede guardar hasta 5mb de información por defecto pero se puede extender con el permiso unlimitedStorage */
  const lightMode = () => {
    $selectors.forEach(el => el.classList.remove(classDark));
    $themeBtn.textContent = moon;
    ls.setItem('theme', 'light');
  };

  const darkMode = () => {
    $selectors.forEach(el => el.classList.add(classDark));
    $themeBtn.textContent = sun;
    ls.setItem('theme', 'dark');
  };

  d.addEventListener('click', e => {
    if (e.target.matches(btn)) {
      // console.log($themeBtn.textContent);
      if ($themeBtn.textContent === moon) {
        darkMode();
      } else {
        lightMode();
      };
    };
  });

  // creamos éste evento para consultar el localStorage del valor almacenado con el fin de cargar esa configuración
  d.addEventListener('DOMContentLoaded', e => {
    // alert('Hola desde la función darktheme');
    if (ls.getItem('theme') === null) ls.setItem('theme', 'light');
    // creamos la variable clave: valor si no existe
    (ls.getItem('theme') === 'light')
      ? lightMode()
      : darkMode();
  });
};