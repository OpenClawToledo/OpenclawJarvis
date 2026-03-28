# Módulo B2B — Portal Empresarial

Adiciona ao projeto base: contas de empresa, preços por grosso, 
pedidos recorrentes, faturação mensal em PDF.

## Ficheiros a copiar para o projeto

```
modules/b2b/java/
  model/
    Company.java          ← conta empresarial (NIF, desconto, condições)
    OrderTemplate.java    ← template de pedido recorrente
    Invoice.java          ← fatura mensal B2B
  controller/
    B2BController.java    ← endpoints /api/b2b/*
  repository/
    CompanyRepository.java
    OrderTemplateRepository.java
    InvoiceRepository.java
```

## Endpoints que adiciona

```
POST /api/b2b/register          ← nova empresa (aguarda aprovação admin)
POST /api/b2b/login
GET  /api/b2b/products          ← catálogo com preços grosso
POST /api/b2b/orders            ← criar pedido
GET  /api/b2b/orders            ← histórico empresa
POST /api/b2b/templates         ← guardar template recorrente
GET  /api/b2b/templates         ← listar templates
POST /api/b2b/templates/{id}/order ← fazer pedido a partir de template
GET  /api/b2b/invoices          ← listar faturas em PDF

GET  /api/admin/b2b/pending     ← empresas por aprovar
POST /api/admin/b2b/{id}/approve
POST /api/admin/invoices/generate ← gerar faturas do mês
```

## application.properties necessário

```properties
feature.b2b=true
b2b.min.order.kg=5
b2b.default.discount.percent=15
b2b.invoice.day=1
```

## Dependência extra no pom.xml (geração de PDF)

```xml
<dependency>
    <groupId>com.itextpdf</groupId>
    <artifactId>itext7-core</artifactId>
    <version>7.2.5</version>
    <type>pom</type>
</dependency>
```
