package com.gabinete.app.config;

import com.gabinete.app.model.Service;
import com.gabinete.app.repository.ServiceRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class DataInitializer implements CommandLineRunner {

    @Autowired
    private ServiceRepository serviceRepository;

    @Override
    public void run(String... args) throws Exception {
        if (serviceRepository.count() == 0) {
            saveService("Contabilidade Organizada", "有组织的会计",
                "Manutenção rigorosa de toda a contabilidade da sua empresa, conforme a legislação portuguesa.",
                "为您的企业提供严格的会计维护，符合葡萄牙法规。", "🧾", 1);

            saveService("Consultoria Fiscal", "税务咨询",
                "Assessoria especializada em IVA, IRC, IRS e optimização fiscal para empresas e particulares.",
                "专业提供增值税、企业所得税及个人所得税咨询与税务优化服务。", "📊", 2);

            saveService("Constituição de Empresas", "公司注册",
                "Apoio completo no processo de criação e registo de novas empresas em Portugal.",
                "全程协助在葡萄牙注册成立新公司的所有程序。", "🏢", 3);

            saveService("Gestão de Salários", "薪资管理",
                "Processamento de salários, declarações à Segurança Social e Autoridade Tributária.",
                "处理薪资、向社会保障局和税务局申报的完整服务。", "📋", 4);

            saveService("Auditoria", "审计",
                "Revisão de contas e auditoria interna para garantir a conformidade e transparência.",
                "财务账目审查与内部审计，确保合规性与透明度。", "🔍", 5);

            saveService("Apoio à Comunidade Chinesa", "华人社区支持",
                "Serviço bilingue especializado para empresários e particulares da comunidade chinesa em Portugal.",
                "为在葡萄牙的华人企业家和个人提供专业双语服务。", "🌏", 6);

            System.out.println("✅ DataInitializer (Gabinete): 6 serviços inseridos.");
        }
    }

    private void saveService(String namePt, String nameZh, String descPt, String descZh, String icon, int order) {
        Service s = new Service();
        s.setNamePt(namePt);
        s.setNameZh(nameZh);
        s.setDescriptionPt(descPt);
        s.setDescriptionZh(descZh);
        s.setIcon(icon);
        s.setDisplayOrder(order);
        s.setActive(true);
        serviceRepository.save(s);
    }
}
