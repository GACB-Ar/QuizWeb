// import hamburgerMenu, { } from "modules/menu_hamburguesa.js";
// import { digitalClock, alarm } from "./dom/reloj.js";
// import countdown from "./dom/cuenta_regresiva.js";
// import scrollTopButton from "modules/boton_scroll.js";
// import darkTheme from "modules/tema_oscuro.js";
// import draw from "./dom/sorteo.js";
// import scrollSpy from "modules/scroll_espia.js";
// import speechReader from "./dom/narrador.js";

const d = document,
  w = window,
  ls = localStorage;


// realizar menú hamburguesa
function hamburgerMenu(panelBtn, panel, menuLink) {
  const d = document;

  d.addEventListener('click', e => {
    if (e.target.matches(panelBtn)
      || e.target.matches(`${panelBtn} *`)) {
      // agregamos el || para hacer que los hijos tambien puedan interactuar con el evento
      d.querySelector(panel).classList.toggle('is-active');
      d.querySelector(panelBtn).classList.toggle('is-active');
      // agregamos la clase también al botón panelBtn para que se cambie de ícono al interactuar
    };
    // Removemos las clases cuando hacen click en algún enlace del menú para que se oculte el mismo
    if (e.target.matches(menuLink)) {
      d.querySelector(panel).classList.remove('is-active');
      d.querySelector(panelBtn).classList.remove('is-active');
    };
  });
};


// Tema oscuro, cambiando con click
function darkTheme(btn, classDark) {
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


// scrollTopButton función para volver al principio
function scrollTopButton(btn) {
  const $scrollBtn = d.querySelector(btn);

  w.addEventListener('scroll', e => {
    let scrollTop = w.pageYOffset || d.documentElement.scrollTop;

    if (scrollTop > 600) {
      $scrollBtn.classList.remove('hidden');
    } else {
      $scrollBtn.classList.add('hidden');
    };
    // console.log(w.pageYOffset, d.documentElement.scrollTop);
  });

  d.addEventListener('click', e => {
    if (e.target.matches(btn)) {
      w.scrollTo({
        behavior: 'smooth',
        top: 0
      });
    };
  });
};


// Identifica en que sección estamos navegando
function scrollSpy() {
  const $sections = d.querySelectorAll('section[data-scroll-spy]');

  const cb = entries => {
    // console.log('entries', entries);

    entries.forEach(entry => {
      // console.log('entry', entry);
      const id = entry.target.getAttribute('id');
      // console.log(id);
      if (entry.isIntersecting) {
        d.querySelector(`a[data-scroll-spy][href='#${id}']`).classList.add('active');
      } else {
        d.querySelector(`a[data-scroll-spy][href='#${id}']`).classList.remove('active');
      };
    });
  };

  const observer = new IntersectionObserver(cb, {
    //root // si la omitimos toma por defecto el document
    // rootMargin: '-250px'
    threshold: [.5, .75]
    //visible cuando está entre el 50% y el 75% del viewport
  });
  // console.log('observer', observer);

  $sections.forEach(el => observer.observe(el));
};


console.clear();


d.addEventListener('DOMContentLoaded', e => {
  hamburgerMenu('.panel-btn', '.panel', '.menu a');
  // primer parámetro el botón del menú
  // segundo parámetro el panel que se va a ocultar
  // 3ro el link que cierra el panel si hacemos click en los enlaces

  // digitalClock('#reloj', '#activar-reloj', '#desactivar-reloj');
  // primer parámetro el div reloj, 2do el botón activar, 3ro el botón parar

  // alarm('/assets/audio/car-alarm.mp3', '#activar-alarma', '#desactivar-alarma');

  // countdown('countdown',
  //   'May 23, 2021 03:23:19',
  //   'Feliz Cumpleaños amigo y docente digital 🤓');

  scrollTopButton('.scroll-top-btn');

  // draw('#winner-btn', '.player');

  scrollSpy();
});

// Lo llamamos fuera del DOMContentLoaded porque internamente la función llama al mismo eventLoader y no funcionaría
darkTheme('.dark-theme-btn', 'dark-mode');
// dark-mode lo llamamos son punto porque lo usaremos en classList

// speechReader();
// Internamente tiene un DOMContentLoaded