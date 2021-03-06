package com.gaugetest.driver;

import com.gaugetest.utils.ReadProperties;
import com.thoughtworks.gauge.AfterScenario;
import com.thoughtworks.gauge.AfterSpec;
import com.thoughtworks.gauge.AfterStep;
import com.thoughtworks.gauge.AfterSuite;
import com.thoughtworks.gauge.BeforeScenario;
import com.thoughtworks.gauge.BeforeSpec;
import com.thoughtworks.gauge.BeforeStep;
import com.thoughtworks.gauge.BeforeSuite;
import com.thoughtworks.gauge.ExecutionContext;
import java.io.IOException;
import java.net.MalformedURLException;
import java.util.ResourceBundle;
import org.apache.commons.lang3.StringUtils;
import org.openqa.selenium.WebDriver;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class DriverCreater {

    private Logger logger = LoggerFactory.getLogger(getClass());
    public static String browserName;
    public static boolean isFullScreen;
    public static WebDriver driver;
    public static String baseUrl;
    public static String osName;
    public static String winHandleBefore;
    public static ResourceBundle ConfigurationProp;
    public static String platformName;

    @BeforeSuite
    public void beforeSuite(ExecutionContext executionContext) {

        logger.info("*************************************************************************" + "\r\n");
        logger.info("------------------------TEST PLAN-------------------------");
    }

    @BeforeSpec
    public void beforeSpec(ExecutionContext executionContext) {
        logger.info("=========================================================================" + "\r\n");
        logger.info("------------------------SPEC-------------------------");
        logger.info("SPEC FILE NAME: " + executionContext.getCurrentSpecification().getFileName());
        logger.info("SPEC NAME: " + executionContext.getCurrentSpecification().getName());
    }

    @BeforeScenario
    public void beforeScenario(ExecutionContext executionContext) throws MalformedURLException, Exception {

        logger.info("_________________________________________________________________________" + "\r\n");
        logger.info("------------------------SCENARIO-------------------------");
        logger.info("SCENARIO NAME: " + executionContext.getCurrentScenario().getName());
        logger.info("SCENARIO TAG: " + executionContext.getCurrentScenario().getTags().toString());

        osName = FindOS.getOperationSystemName();
        ConfigurationProp = ReadProperties.readProp("Configuration.properties");
        String key = System.getenv("key");
        browserName = ConfigurationProp.getString("browserName");
        baseUrl = ConfigurationProp.getString("baseUrl");
        isFullScreen = Boolean.parseBoolean(ConfigurationProp.getString("isFullScreen"));
            platformName = FindOS.getOperationSystemNameExpanded();
            driver = LocalBrowserExec.LocalExec(browserName);
        driver.get(baseUrl);
        winHandleBefore = driver.getWindowHandle();
    }

    @BeforeStep
    public void beforeStep(ExecutionContext executionContext) {

        //logger.info(executionContext.getCurrentStep().getText());
        //logger.info("?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????");
        logger.info(executionContext.getCurrentStep().getDynamicText());
    }

    @AfterStep
    public void afterStep(ExecutionContext executionContext) throws IOException {

        if (executionContext.getCurrentStep().getIsFailing()) {

            logger.error(executionContext.getCurrentSpecification().getFileName());
            logger.error("Message: " + executionContext.getCurrentStep().getErrorMessage() + "\r\n"
                    + executionContext.getCurrentStep().getStackTrace());
        }
        logger.info("?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????");
    }

    @AfterScenario
    public void afterScenario(ExecutionContext executionContext) {

        quitDriver();
        if (executionContext.getCurrentScenario().getIsFailing()) {

            logger.info("TEST BA??ARISIZ");
        } else {

            logger.info("TEST BA??ARILI");
        }

        logger.info("_________________________________________________________________________" + "\r\n");
    }

    @AfterSpec
    public void afterSpec(ExecutionContext executionContext) {

        logger.info("=========================================================================" + "\r\n");
    }

    @AfterSuite
    public void afterSuite(ExecutionContext executionContext) {

        logger.info("*************************************************************************" + "\r\n");
    }

    private void quitDriver(){

        if(driver != null){
            driver.quit();
            logger.info("Driver kapat??ld??.");
        }
    }




}
