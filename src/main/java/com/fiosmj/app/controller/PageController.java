package com.fiosmj.app.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class PageController {

    @GetMapping("/obrigado")
    @ResponseBody
    public String obrigado() {
        return """
            <!DOCTYPE html>
            <html lang="pt-BR">
            <head>
              <meta charset="UTF-8"/>
              <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
              <title>Pedido Confirmado – Fios MJ</title>
              <style>
                * { box-sizing: border-box; margin: 0; padding: 0; }
                body { font-family: 'Segoe UI', sans-serif; background: #fff5fb; min-height: 100vh;
                       display: flex; align-items: center; justify-content: center; padding: 20px; }
                .card { background: white; border-radius: 20px; padding: 48px 40px; max-width: 480px;
                        width: 100%; text-align: center; box-shadow: 0 8px 40px rgba(233,30,123,0.12); }
                .icon { font-size: 4rem; margin-bottom: 20px; }
                h1 { color: #e91e7b; font-size: 1.8rem; margin-bottom: 12px; }
                p { color: #666; font-size: 1rem; line-height: 1.6; margin-bottom: 24px; }
                a { display: inline-block; background: #e91e7b; color: white; padding: 14px 32px;
                    border-radius: 10px; text-decoration: none; font-weight: 700; font-size: 1rem; }
                a:hover { opacity: 0.9; }
              </style>
            </head>
            <body>
              <div class="card">
                <div class="icon">🧶✅</div>
                <h1>Pedido Confirmado!</h1>
                <p>Obrigada pela sua compra! 💕<br>
                   Em breve entraremos em contato via WhatsApp para confirmar os detalhes e o prazo de entrega.</p>
                <a href="/">Ver mais produtos</a>
              </div>
            </body>
            </html>
            """;
    }

    @GetMapping("/pendente")
    @ResponseBody
    public String pendente() {
        return """
            <!DOCTYPE html>
            <html lang="pt-BR">
            <head>
              <meta charset="UTF-8"/>
              <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
              <title>Pagamento em Análise – Fios MJ</title>
              <style>
                * { box-sizing: border-box; margin: 0; padding: 0; }
                body { font-family: 'Segoe UI', sans-serif; background: #fff5fb; min-height: 100vh;
                       display: flex; align-items: center; justify-content: center; padding: 20px; }
                .card { background: white; border-radius: 20px; padding: 48px 40px; max-width: 480px;
                        width: 100%; text-align: center; box-shadow: 0 8px 40px rgba(233,30,123,0.12); }
                .icon { font-size: 4rem; margin-bottom: 20px; }
                h1 { color: #f59e0b; font-size: 1.8rem; margin-bottom: 12px; }
                p { color: #666; font-size: 1rem; line-height: 1.6; margin-bottom: 24px; }
                a { display: inline-block; background: #e91e7b; color: white; padding: 14px 32px;
                    border-radius: 10px; text-decoration: none; font-weight: 700; font-size: 1rem; }
                a:hover { opacity: 0.9; }
              </style>
            </head>
            <body>
              <div class="card">
                <div class="icon">🧶⏳</div>
                <h1>Pagamento em Análise</h1>
                <p>Seu pagamento está sendo processado.<br>
                   Assim que for confirmado, entraremos em contato via WhatsApp! 💕</p>
                <a href="/">Voltar à loja</a>
              </div>
            </body>
            </html>
            """;
    }
}
