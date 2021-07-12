import React, { useEffect, useState } from "react";
import styled from "@emotion/styled";
import HeaderComponent from "../../Components/Header";
import { useLocation, useHistory } from "react-router-dom";
import axios from "axios";
import Text from "antd/lib/typography/Text";
import MathJax from "react-mathjax";
import { Input, Button, Row, Col, Divider, Form, notification } from "antd";
import { useForm } from "antd/lib/form/Form";
const { TextArea } = Input;

const Header = styled("div")`
  height: 100px;
  width: 100%;
  background-color: #6d60b0;
  padding: 0px 70px 0px 70px;
`;
const Wrapper = styled("div")`
  background: #f4f8f9;
  height: 100vh;
  width: 100%;
`;

const BodyContainer = styled("div")`
  padding: 70px 70px 0px 70px;
`;

const PracticeContainer = styled("div")`
  padding-top: 40px;
  display: flex;
  justify-content: space-between;
`;

const QuestionContainer = styled("div")`
  padding: 18px 18px 18px 18px;
  box-shadow: 0 4px 6px rgb(0 0 0 / 10%), 0 1px 3px rgb(0 0 0 / 10%);
  background-color: #fff;
  border-radius: 4px;
`;

const InstructionContainer = styled("div")`
  padding: 30px;
  box-shadow: 0 4px 6px rgb(0 0 0 / 10%), 0 1px 3px rgb(0 0 0 / 10%);
  background-color: #fff;
  border-radius: 4px;
`;

const StyledButton = styled(Button)`
  background: #6d60b0;
  color: white;
  border-radius: 5px;
  height: 40px;
  &:hover,
  &:focus {
    background: #6d60b0;
    color: white;
  }
  border: none;
`;

const PracticeBoard = () => {
  const location: any = useLocation();
  const id = location.state.id;
  const name = location.state.name;
  const studentTopicId = location.state.studentTopicId;
  const [allQuestions, setAllQuestions] = useState<any>();
  const [isDisabled, setIsDisabled] = useState<boolean>(true);
  const [inputAnswer, setInputAnswer] = useState("");
  const [correct, setCorrect] = useState<number>(0);
  const [totalAttempts, setTotalAttempts] = useState<number>(0);
  const [help, setHelp] = useState<any>();
  const [isGetHelp, setIsGetHelp] = useState<boolean>(false);
  const [correctPopover, setCorrectPopover] = useState<boolean>(false);
  const history = useHistory();
  const [disbaleCheck, setDisableCheck] = useState<boolean>(false);

  var initialTime = performance.now();

  const [form] = useForm();

  const fetchAllQuestions = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/getQuestion/${id}`);
      setAllQuestions(response);
    } catch (e) {}
  };

  useEffect(() => {
    fetchAllQuestions();
  }, []);

  const getHelp = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/getHelp", {
        question: allQuestions.data.title,
        answer: allQuestions.data.answer,
        effort: inputAnswer,
        topic: id,
      });

      setHelp(response.data.get_help);
      setIsGetHelp(true);
    } catch (e) {}
  };

  const handleChange = (e: any) => {
    const inputValue = e.target.value;
    setInputAnswer(inputValue);
    if (inputValue.length > 0) {
      setIsDisabled(false);
    }
    if (inputValue.length > 0 && disbaleCheck) {
      setIsDisabled(true);
    }
    if (inputValue.length === 0) {
      setIsDisabled(true);
    }
  };

  const onCorrectAttempt = () => {
    notification.success({
      message: "Correct",
      description: "Your answer is correct.",
      duration: 2,
    });
  };
  const onInCorrectAttempt = () => {
    notification.error({
      message: "Incorrect",
      description: "Your answer is incorrect. See the help section for correct answer.",
      duration: 2,
    });
  };

  const handleCheckAnswer = () => {
    setTotalAttempts(totalAttempts + 1);
    const inputAnswerStringify = inputAnswer.toString();
    const correctAnswerStringify = allQuestions.data.answer.toString();

    if (inputAnswerStringify === correctAnswerStringify) {
      form.setFieldsValue({ userinput: "" });
      setCorrectPopover(true);
      setCorrect(correct + 1);
      setIsGetHelp(false);
      handleNextQuestion();
      onCorrectAttempt();
    } else {
      getHelp();
      setDisableCheck(true);
      setIsDisabled(true);
      onInCorrectAttempt();
    }
  };

  const handleNextQuestion = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/getQuestion/${id}`);
      setAllQuestions(response);
      setDisableCheck(false);
      setIsGetHelp(false);
      form.setFieldsValue({ userinput: "" });
    } catch (e) {}
  };

  const handleMenu = async () => {
    const finalTime = performance.now();
    const differenceInSeconds = finalTime - initialTime;
    const timeTaken = new Date(differenceInSeconds).toISOString().substr(11, 8);

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/submit", {
        student_topic_id: studentTopicId,
        topic_id: id,
        total_attempts: totalAttempts,
        correct_answer: correct,
        has_passed: correct >= 5 ? true : false,
        time_taken: timeTaken,
      });
      history.push("/home");
    } catch (e) {}
  };

  return (
    <Wrapper>
      <MathJax.Provider>
        <Header>
          <HeaderComponent />
        </Header>
        <BodyContainer>
          <Row gutter={64}>
            <Col span={16}>
              <QuestionContainer>
                <div style={{ display: "flex", justifyContent: "space-between" }}>
                  <div>
                    <Text style={{ fontSize: "20px", fontWeight: 600, paddingRight: "10px" }}>
                      {name} :
                    </Text>

                    {allQuestions && allQuestions.data && allQuestions.data.title && (
                      <Text style={{ fontSize: "18px" }}>
                        <MathJax.Node
                          inline
                          formula={allQuestions && allQuestions.data && allQuestions.data.title}
                        />
                      </Text>
                    )}
                  </div>
                </div>

                <Divider orientation="left">Answer</Divider>
                <Form name="basic" form={form}>
                  <Row gutter={64}>
                    <Col xs={24} sm={24} md={10}>
                      <Form.Item name="userinput">
                        <TextArea rows={4} onChange={handleChange} />
                      </Form.Item>
                    </Col>

                    <Col xs={24} sm={24} md={7}>
                      <div style={{ display: "flex", flexDirection: "column", gap: "5px" }}>
                        <Text style={{ fontSize: "18px", fontWeight: 600 }}>Correct</Text>
                        <Text style={{ fontSize: "18px", fontWeight: 600 }}>{correct}</Text>
                      </div>
                    </Col>
                    <Col xs={24} sm={24} md={7}>
                      <div style={{ display: "flex", flexDirection: "column", gap: "5px" }}>
                        <Text style={{ fontSize: "18px", fontWeight: 600 }}>Total Attempts</Text>
                        <Text style={{ fontSize: "18px", fontWeight: 600 }}>{totalAttempts}</Text>
                      </div>
                    </Col>
                  </Row>
                </Form>

                <Row gutter={12} style={{ marginTop: "12px", paddingTop: "15px" }}>
                  <Col xs={24} sm={3}>
                    <StyledButton onClick={handleMenu}>Menu</StyledButton>
                  </Col>
                  <Col xs={15} sm={4}>
                    <StyledButton disabled={isDisabled} onClick={handleCheckAnswer}>
                      Check Answer
                    </StyledButton>
                  </Col>
                  <Col xs={24} sm={3}>
                    <StyledButton onClick={handleNextQuestion}>Next Question</StyledButton>
                  </Col>
                </Row>
              </QuestionContainer>
              <div style={{ marginTop: "30px" }}>
                {isGetHelp && (
                  <QuestionContainer>
                    <Text style={{ fontSize: "20px", fontWeight: 600 }}>Help:</Text>
                    <div style={{ paddingTop: "15px" }}>
                      <Text style={{ fontSize: "18px" }}>{help}</Text>
                    </div>
                  </QuestionContainer>
                )}
              </div>
            </Col>
            <Col span={8}>
              <InstructionContainer>
                <div style={{ paddingBottom: "10px" }}>
                  <Text style={{ fontSize: "20px", fontWeight: 600 }}>Instructions:</Text>
                </div>
                {allQuestions &&
                  allQuestions.data &&
                  allQuestions.data.instructions.map((item: any, index: any) => (
                    <div key={index} style={{ paddingBottom: "5px" }}>
                      <Text style={{ fontSize: "17px" }}>{item}</Text>
                    </div>
                  ))}
                {allQuestions && allQuestions.data && allQuestions.data.video_link && (
                  <div style={{ display: "flex", justifyContent: "center", paddingTop: "6px" }}>
                    <a
                      href={allQuestions && allQuestions.data && allQuestions.data.video_link}
                      target="_blank"
                      style={{ textTransform: "uppercase", fontSize: "17px" }}
                    >
                      watch video
                    </a>
                  </div>
                )}
              </InstructionContainer>
            </Col>
          </Row>
        </BodyContainer>
      </MathJax.Provider>
    </Wrapper>
  );
};

export default PracticeBoard;
