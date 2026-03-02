// Script para alternar entre tema claro e escuro

(function() {
    // Detectar preferência do sistema
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    // Obter tema salvo no localStorage ou usar padrão do sistema
    const savedTheme = localStorage.getItem('theme');
    const initialTheme = savedTheme || (prefersDark ? 'dark' : 'dark');
    
    // Aplicar tema inicial
    document.documentElement.setAttribute('data-theme', initialTheme);
    
    // Obter botão de toggle
    const themeBtn = document.getElementById('theme-toggle');
    
    // Alternar tema
    themeBtn.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        // Aplicar novo tema
        document.documentElement.setAttribute('data-theme', newTheme);
        
        // Salvar preferência
        localStorage.setItem('theme', newTheme);
        
        // Feedback visual
        themeBtn.style.transform = 'rotate(20deg)';
        setTimeout(() => {
            themeBtn.style.transform = '';
        }, 300);
    });
    
    // Detectar mudança de preferência do sistema
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (!localStorage.getItem('theme')) {
            const newTheme = e.matches ? 'dark' : 'light';
            document.documentElement.setAttribute('data-theme', newTheme);
        }
    });
})();
