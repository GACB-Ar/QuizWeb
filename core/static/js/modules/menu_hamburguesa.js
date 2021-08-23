// realizar menú hamburguesa
export default function hamburgerMenu(panelBtn, panel, menuLink) {
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