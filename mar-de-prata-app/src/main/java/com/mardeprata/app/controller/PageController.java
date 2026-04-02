package com.mardeprata.app.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class PageController {

    @GetMapping("/admin")
    public String admin() {
        return "forward:/admin/index.html";
    }

    @GetMapping("/admin/")
    public String adminSlash() {
        return "forward:/admin/index.html";
    }
}
