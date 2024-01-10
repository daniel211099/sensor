################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (11.3.rel1)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Core/Src/Data/sensor.c \
../Core/Src/Data/uart_data.c 

OBJS += \
./Core/Src/Data/sensor.o \
./Core/Src/Data/uart_data.o 

C_DEPS += \
./Core/Src/Data/sensor.d \
./Core/Src/Data/uart_data.d 


# Each subdirectory must supply rules for building sources it contributes
Core/Src/Data/%.o Core/Src/Data/%.su Core/Src/Data/%.cyclo: ../Core/Src/Data/%.c Core/Src/Data/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F411xE -c -I../Core/Inc -I../Drivers/STM32F4xx_HAL_Driver/Inc -I../Drivers/STM32F4xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F4xx/Include -I../Drivers/CMSIS/Include -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Core-2f-Src-2f-Data

clean-Core-2f-Src-2f-Data:
	-$(RM) ./Core/Src/Data/sensor.cyclo ./Core/Src/Data/sensor.d ./Core/Src/Data/sensor.o ./Core/Src/Data/sensor.su ./Core/Src/Data/uart_data.cyclo ./Core/Src/Data/uart_data.d ./Core/Src/Data/uart_data.o ./Core/Src/Data/uart_data.su

.PHONY: clean-Core-2f-Src-2f-Data

